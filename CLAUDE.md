# Agentic Engineer

## Context

This project is a boilerplate template for starting a new project that will utilize Claude Code and other agents for development assistance. We will use TypeScript/Node.js with a focus on clean architecture and test-driven development.

## Tooling

- Frontend:
  - 
- Backend:
  - 

- Always use 'uv' over 'pip' or 'poetry'

## Key Commands
- `uv run pytest` - Run tests

## Project Structure
- `apps/frontend/` - Frontend source code
- `apps/frontend/` - Frontend source code
- `docs/` - Additional documentation

## Development Guidelines
1. Write tests first (TDD)
2. Use TypeScript strict mode
3. Follow existing naming conventions
4. Add JSDoc for public APIs
5. Keep functions under 50 lines

## Important Notes
- Always validate inputs using Zod schemas
- Use Result<T,E> pattern for error handling
- Database querires go through repository pattern
- API responses use standardized format
- For python types, never use Dict, always use a concrete pydantic model with typed fields