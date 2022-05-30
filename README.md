# E-commerce [microservice]
![Python3](https://img.shields.io/badge/language-python3-brightgreen)
![Django](https://img.shields.io/badge/backend-django-brightgreen)
![SQL](https://img.shields.io/badge/sql-postgres-brightgreen)
![NoSQL](https://img.shields.io/badge/nosql-redis-brightgreen)

An e-commerce backend built using microservice architecture, with an immediately consistent ordering system.

This is an improvement of the monolithic e-commerce application build [here](https://github.com/harsh020/ecommerce-monolith).

## Design Overview

![Ecommerce](https://user-images.githubusercontent.com/39561084/171032060-29bd3468-5359-4e11-ac89-2d8b27969541.jpg)

Patterns and Principles used
- SOLID
- Strategy Pattern
- Decorator Pattern
- API Gateway Pattern
- Service Aggregator Pattern

## Future Scopes

- Building a highly available searching and injestion service.
- Implemting cache
- Converting Ordering Service Aggregator Pattern to Saga Pattern to allow rollbacks.
