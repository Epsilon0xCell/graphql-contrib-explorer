# graphql-contrib-explorer

I built this as part of my GitHub Developer Program portfolio. It talks to the GitHub GraphQL API and draws one readable picture of a user's work: the contribution graph across repositories, the organizations that work passes through, and how the effort clusters over time. It is the map I want in hand before I read a single line of anyone's code, including my own.

Status: scaffold. The interface is defined and the query engine is the next build step.

## What it will do

- Query a user's contribution calendar and totals through the GraphQL API
- List the organizations the user belongs to and the work tied to each one
- Group contributions by repository, with the busiest periods marked
- Print the map as a plain text report a reader can verify against the profile

Built by Gavin Blacklock (Epsilon0xCell).
