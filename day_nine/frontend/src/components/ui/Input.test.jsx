import { describe, it, expect, vi } from 'vitest'
import { render, screen } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import { Input } from './Input.jsx'

describe('Input', () => {
  it('should render a text input by default', () => {
    render(<Input />)
    expect(screen.getByRole('textbox')).toBeInTheDocument()
  })

  it('should render a textarea when type is textarea', () => {
    render(<Input type="textarea" />)
    expect(screen.getByRole('textbox').tagName).toBe('TEXTAREA')
  })

  it('should call onChange with the new value', async () => {
    const onChange = vi.fn()
    render(<Input onChange={onChange} />)
    await userEvent.type(screen.getByRole('textbox'), 'hello')
    expect(onChange).toHaveBeenLastCalledWith('hello')
  })

  it('should render error message when error prop provided', () => {
    render(<Input placeholder="Email" error="Required" />)
    expect(screen.getByText('Required')).toBeInTheDocument()
  })
})
