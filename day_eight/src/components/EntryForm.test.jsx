import { describe, it, expect, vi } from 'vitest'
import { render, screen } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import { EntryForm } from './EntryForm.jsx'

describe('EntryForm', () => {
  it('should render a title input', () => {
    render(<EntryForm onSubmit={() => {}} />)
    expect(screen.getByPlaceholderText('Title')).toBeInTheDocument()
  })

  it('should render a submit button', () => {
    render(<EntryForm onSubmit={() => {}} />)
    expect(screen.getByRole('button', { name: /add/i })).toBeInTheDocument()
  })
})
