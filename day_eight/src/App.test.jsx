import { describe, it, expect } from 'vitest'
import { render, screen } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import App from './App.jsx'

describe('App', () => {
  it('should show a submitted entry in the grid', async () => {
    render(<App />)
    await userEvent.type(screen.getByPlaceholderText('Title'), 'My first entry')
    await userEvent.type(screen.getByPlaceholderText('Body'), 'Some body text')
    await userEvent.click(screen.getByText('Add'))
    expect(screen.getByText('My first entry')).toBeInTheDocument()
  })
})
