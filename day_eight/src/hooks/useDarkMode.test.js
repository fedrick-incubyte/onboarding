import { describe, it, expect, vi, beforeEach } from 'vitest'
import { renderHook, act } from '@testing-library/react'
import { useDarkMode } from './useDarkMode.js'

beforeEach(() => {
  document.documentElement.classList.remove('dark')
})

describe('useDarkMode', () => {
  it('should return false when system preference is light', () => {
    vi.stubGlobal('matchMedia', () => ({ matches: false }))
    const { result } = renderHook(() => useDarkMode())
    expect(result.current[0]).toBe(false)
  })

  it('should add the dark class to documentElement when darkMode is true', () => {
    const { result } = renderHook(() => useDarkMode())
    act(() => result.current[1]())
    expect(document.documentElement.classList.contains('dark')).toBe(true)
  })
})
