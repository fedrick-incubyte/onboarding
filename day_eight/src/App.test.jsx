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

  it('should show only matching entries when a tag is selected', async () => {
    render(<App />)
    await userEvent.type(screen.getByPlaceholderText('Title'), 'React entry')
    await userEvent.type(screen.getByPlaceholderText('Body'), 'body')
    await userEvent.type(screen.getByPlaceholderText('Tags'), 'react')
    await userEvent.click(screen.getByText('Add'))
    await userEvent.type(screen.getByPlaceholderText('Title'), 'Other entry')
    await userEvent.type(screen.getByPlaceholderText('Body'), 'body')
    await userEvent.click(screen.getByText('Add'))
    await userEvent.click(screen.getByText('react'))
    expect(screen.getByText('React entry')).toBeInTheDocument()
    expect(screen.queryByText('Other entry')).not.toBeInTheDocument()
  })
})
