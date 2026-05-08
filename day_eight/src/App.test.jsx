import { describe, it, expect, beforeEach, afterEach, vi } from 'vitest'
import { render, screen } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import App from './App.jsx'

const localStorageMock = (() => {
  let store = {}
  return {
    getItem: (key) => store[key] ?? null,
    setItem: (key, value) => { store[key] = String(value) },
    clear: () => { store = {} },
    removeItem: (key) => { delete store[key] },
  }
})()

beforeEach(() => {
  vi.stubGlobal('localStorage', localStorageMock)
  localStorageMock.clear()
  document.documentElement.classList.remove('dark')
})

afterEach(() => {
  vi.unstubAllGlobals()
})

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
    await userEvent.click(screen.getAllByText('react')[0])
    expect(screen.getByText('React entry')).toBeInTheDocument()
    expect(screen.queryByText('Other entry')).not.toBeInTheDocument()
  })

  it('should persist entries across remounts', async () => {
    const { unmount } = render(<App />)
    await userEvent.type(screen.getByPlaceholderText('Title'), 'Persisted entry')
    await userEvent.type(screen.getByPlaceholderText('Body'), 'body')
    await userEvent.click(screen.getByText('Add'))
    unmount()
    render(<App />)
    expect(screen.getByText('Persisted entry')).toBeInTheDocument()
  })

  it('should render the app title', () => {
    render(<App />)
    expect(screen.getByText('Craftlog')).toBeInTheDocument()
  })

  it('should toggle dark mode on documentElement when dark mode toggle is clicked', async () => {
    render(<App />)
    await userEvent.click(screen.getByRole('switch'))
    expect(document.documentElement.classList.contains('dark')).toBe(true)
  })
})
