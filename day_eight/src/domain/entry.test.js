import { describe, it, expect } from 'vitest'
import { createEntry } from './entry.js'

describe('createEntry', () => {
  it('should return an object with id, title, body, tags, and createdAt', () => {
    const entry = createEntry('My title', 'My body', ['tag1'])
    expect(entry).toHaveProperty('id')
    expect(entry).toHaveProperty('title', 'My title')
    expect(entry).toHaveProperty('body', 'My body')
    expect(entry).toHaveProperty('tags')
    expect(entry).toHaveProperty('createdAt')
  })

  it('should give each entry a unique id', () => {
    const a = createEntry('Title A', 'Body A', [])
    const b = createEntry('Title B', 'Body B', [])
    expect(a.id).not.toBe(b.id)
  })

  it('should throw when title is empty', () => {
    expect(() => createEntry('', 'Some body', [])).toThrow('Title is required')
  })

  it('should throw when title exceeds 100 characters', () => {
    const longTitle = 'a'.repeat(101)
    expect(() => createEntry(longTitle, 'Some body', [])).toThrow('Title too long')
  })

  it('should throw when body is empty', () => {
    expect(() => createEntry('Some title', '', [])).toThrow('Body is required')
  })

  it('should trim whitespace from title and body', () => {
    const entry = createEntry('  My title  ', '  My body  ', [])
    expect(entry.title).toBe('My title')
    expect(entry.body).toBe('My body')
  })
})
