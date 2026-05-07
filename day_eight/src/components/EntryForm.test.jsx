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

  it('should call onSubmit with the entry when submitted', async () => {
    const onSubmit = vi.fn()
    render(<EntryForm onSubmit={onSubmit} />)
    await userEvent.type(screen.getByPlaceholderText('Title'), 'My title')
    await userEvent.type(screen.getByPlaceholderText('Body'), 'My body')
    await userEvent.click(screen.getByRole('button', { name: /add/i }))
    expect(onSubmit).toHaveBeenCalledOnce()
    const entry = onSubmit.mock.calls[0][0]
    expect(entry.title).toBe('My title')
    expect(entry.body).toBe('My body')
  })

  it('should clear the title field after a successful submission', async () => {
    render(<EntryForm onSubmit={() => {}} />)
    await userEvent.type(screen.getByPlaceholderText('Title'), 'Some title')
    await userEvent.type(screen.getByPlaceholderText('Body'), 'Some body')
    await userEvent.click(screen.getByRole('button', { name: /add/i }))
    expect(screen.getByPlaceholderText('Title')).toHaveValue('')
  })
})
