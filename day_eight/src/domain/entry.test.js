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
})
