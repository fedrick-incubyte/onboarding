import { describe, it, expect } from 'vitest'
import { parseTag } from './tag.js'

describe('parseTag', () => {
  it('should lowercase and trim a tag', () => {
    expect(parseTag('  React  ')).toBe('react')
  })
})
