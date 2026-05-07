import { describe, it, expect } from 'vitest'
import { render, screen } from '@testing-library/react'
import { Card } from './Card.jsx'

describe('Card', () => {
  it('should render children', () => {
    render(<Card>Hello Card</Card>)
    expect(screen.getByText('Hello Card')).toBeInTheDocument()
  })

  it('should render Card.Header children', () => {
    render(<Card.Header>Header content</Card.Header>)
    expect(screen.getByText('Header content')).toBeInTheDocument()
  })
})
