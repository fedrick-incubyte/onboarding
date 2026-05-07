import { describe, it, expect } from 'vitest'
import { formatDate } from './date.js'

describe('formatDate', () => {
  it('should format an ISO date as a human-readable string', () => {
    const result = formatDate('2024-01-15T10:30:00.000Z')
    expect(result).toMatch(/Jan/)
    expect(result).toMatch(/2024/)
  })
})
