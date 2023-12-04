import express from 'express'
import bodyParser from 'body-parser'
import { Request, Response, NextFunction } from 'express'
import { App } from './app'
import { Prisma } from '@prisma/client'
import { PrismaBikeRepo } from './external/database/prisma-bike-repo'
import { PrismaUserRepo } from './external/database/prisma-user-repo'
import { PrismaRentRepo } from './external/database/prisma-rent-repo'



const cors = (req: Request, res: Response, next: NextFunction): void => {
    res.set('Access-Control-Allow-Origin', '*');
    res.set('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE');
    res.set('Access-Control-Allow-Headers', 'Content-Type, Authorization');
    next();
}


const contentType = (req: Request, res: Response, next: NextFunction): void => {
    res.type('json');
    next();
}


const server = express();
server.use(bodyParser.json());
server.use(cors);
server.use(contentType);

const app = new App(
    new PrismaUserRepo(),
    new PrismaBikeRepo(),
    new PrismaRentRepo());

server.post('/api/users', async (req, res) => {
    try{
        const id = await App.registerUser(req.body)
        res.status(201).json({ id })
    } catch (err) {
        if (err instanceof Prisma.PrismaClientKnownRequestError) {
            if (err.code === 'P2002') {
                res.status(400).json({ error: 'Email already exists' });
            }
        }
        res.status(500).json({ error: 'Internal server error' });
    }
})

const port = process.env.PORT || 3000;
server.listen(port, () => {
    console.log(`Server listening on port ${port}`);
})

export default server
