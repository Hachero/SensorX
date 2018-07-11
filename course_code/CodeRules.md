# Code Writing Notes

## Meaningful Names

- Avoid encoding schemes that are not obvious
- Don't use puns
- Classes are Nouns
- Methods are Verbs
- Use a single word (i.e. fetch/retriece/get pick one and stick with it -consistency in context)

## Functions

- Keep them small
- Do only one thing
- Statements within a function are all at the same level of abstraction
- don't add hidden side effects
- Functions either *do* something or *answer* something but not both

## Comments

Avoid commenting by making the code express the intent

## Testing

- **First** Law You may not write production code until you have written a failing unit test.
- **Second** Law You may not write more of a unit test than is sufficient to fail, and not compiling is failing.
- **Third** Law You may not write more production code than is sufficient to pass the currently failing test.
