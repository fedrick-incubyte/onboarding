import { validateTask } from './task'

it('should_throw_when_title_is_empty', () => {
  expect(() => validateTask({ title: '' })).toThrow('Title is required')
})

it('should_throw_when_title_exceeds_200_characters', () => {
  expect(() => validateTask({ title: 'a'.repeat(201) })).toThrow('Title too long')
})
