import { describe, it, expect } from 'vitest'
import { parseTag, getAllTags } from './tag.js'

describe('parseTag', () => {
  it('should lowercase and trim a tag', () => {
    expect(parseTag('  React  ')).toBe('react')
  })

  it('should return null for an empty string', () => {
    expect(parseTag('   ')).toBeNull()
  })
})

describe('getAllTags', () => {
  it('should return all unique tags from entries', () => {
    const entries = [
      { tags: ['react', 'js'] },
      { tags: ['react', 'css'] },
    ]
    expect(getAllTags(entries)).toEqual(['react', 'js', 'css'])
  })
})
