import { useCallback, useEffect, useRef, useState } from 'react'
import './BackgroundMusic.css'

const musicSource = import.meta.env.BASE_URL + 'audio/choral-chambers.mp3'

type PlaybackState = 'loading' | 'playing' | 'blocked' | 'paused' | 'error'

function BackgroundMusic() {
  const audioRef = useRef<HTMLAudioElement>(null)
  const manuallyPausedRef = useRef(false)
  const [playbackState, setPlaybackState] = useState<PlaybackState>('loading')

  const startPlayback = useCallback(async () => {
    const audio = audioRef.current
    if (!audio) return

    try {
      await audio.play()
      setPlaybackState(audio.paused ? 'paused' : 'playing')
    } catch (error) {
      const errorName = error instanceof Error ? error.name : ''
      if (errorName === 'NotAllowedError') {
        setPlaybackState('blocked')
      } else if (errorName !== 'AbortError') {
        setPlaybackState('error')
      }
    }
  }, [])

  useEffect(() => {
    const audio = audioRef.current
    if (!audio) return

    audio.volume = 0.45
    const handlePlay = () => setPlaybackState('playing')
    const handlePause = () => setPlaybackState('paused')
    const handleError = () => setPlaybackState('error')

    audio.addEventListener('play', handlePlay)
    audio.addEventListener('pause', handlePause)
    audio.addEventListener('error', handleError)
    void startPlayback()

    return () => {
      audio.removeEventListener('play', handlePlay)
      audio.removeEventListener('pause', handlePause)
      audio.removeEventListener('error', handleError)
    }
  }, [startPlayback])

  useEffect(() => {
    if (playbackState !== 'blocked') return

    const resumeAfterGesture = (event: Event) => {
      if (event.target instanceof Element && event.target.closest('.music-control')) return
      if (!manuallyPausedRef.current) void startPlayback()
    }

    window.addEventListener('click', resumeAfterGesture)
    window.addEventListener('keydown', resumeAfterGesture)
    return () => {
      window.removeEventListener('click', resumeAfterGesture)
      window.removeEventListener('keydown', resumeAfterGesture)
    }
  }, [playbackState, startPlayback])

  const togglePlayback = () => {
    const audio = audioRef.current
    if (!audio) return

    if (playbackState === 'playing') {
      manuallyPausedRef.current = true
      audio.pause()
    } else {
      manuallyPausedRef.current = false
      void startPlayback()
    }
  }

  const isPlaying = playbackState === 'playing'
  const label = playbackState === 'error'
    ? '音乐不可用'
    : isPlaying ? '暂停音乐'
      : playbackState === 'blocked' ? '点击播放音乐' : '播放音乐'
  const description = playbackState === 'blocked'
    ? '浏览器限制有声自动播放，请点击播放音乐'
    : label

  return (
    <>
      <audio ref={audioRef} src={musicSource} preload="auto" loop aria-hidden="true" />
      <button
        className={'music-control' + (isPlaying ? ' is-playing' : '')}
        type="button"
        onClick={togglePlayback}
        aria-label={description}
        aria-pressed={isPlaying}
        disabled={playbackState === 'error'}
        title={description}
      >
        <span className="music-bars" aria-hidden="true"><i /><i /><i /></span>
        <span aria-live="polite">{label}</span>
      </button>
    </>
  )
}

export default BackgroundMusic
