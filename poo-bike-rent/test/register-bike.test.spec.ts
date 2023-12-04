import { User } from './../src/user';
import request from 'supertest';
import server from '../src/server';
import prisma from '../src/external/database/db';


describe('Register User', () => {
    beforeEach(async () => {
        await prisma.user.deleteMany({})
    })

    afterAll(async () => {
        await prisma.$disconnect()
    })

    it('registers a bike with valid data', async () => {
        await request(server)
            .post('/api/bikes')
                import request from 'supertest'
                import server from '../src/server'
                import prisma from '../src/external/database/db'
            
            describe('Register bike route', () => {
                beforeEach(async () => {
                    await prisma.bike.deleteMany({})
                })
            
                afterAll(async () => {
                    await prisma.bike.deleteMany({})
                })
            
                it('registers a bike with valid data', async () => {
                    await request(server)
                        .post('/api/bikes')
                        .send({
                            name: 'Caloi Mountain Bike',
                            type: 'mountain bike',
                            bodysize: 1234,
                            maxLoad: 1234,
                            rate: 100.0,
                            description: 'My bike',
                            ratings: 5,
                            imageURLs: []
                        })
                        .expect(201)
                        .then((res) => {
                            expect(res.body.id).toBeDefined()
                        })
                })
            
                it.only('returns 400 when trying to register duplicate user', async () => {
                    await request(server)
                        .post('/api/users')
                        .send({
                            name: 'Caloi Mountain Bike',
                            type: 'mountain bike',
                            bodysize: 1234,
                            maxLoad: 1234,
                            rate: 100.0,
                            description: 'My bike',
                            ratings: 5,
                            imageURLs: []
                        })
                        .expect(201)
            
                    await request(server)
                        .post('/api/bikes')
                        .send({
                            name: 'Caloi Mountain Bike',
                            type: 'mountain bike',
                            bodysize: 1234,
                            maxLoad: 1234,
                            rate: 100.0,
                            description: 'My bike',
                            ratings: 5,
                            imageURLs: []
                        })
                        .expect(400)
                }, 20000)
            })

            .send({
                name: 'Caloi Mountain Bike',
                type: 'mountain bike',
                bodysize: 1234,
                maxLoad: 1234,
                rate: 100.0,
                description: 'My bike',
                ratings: 5,
                imageURLs: []
            })
            .expect(201)
            .then((res) => {
                expect(res.body.id).toBeDefined()
            })
    }, 20000)
})
