import { useState } from 'react'
import type { WelcomePageProps } from './WelcomePage'
import '../App.css'
import logo from '../assets/nittanyride-logo.png'

type LoginPageProps = {
    onLogin: (user: WelcomePageProps) => void
}

function formatRole(role:string): WelcomePageProps['role'] | null {
    if (role === 'rider') {
        return 'Rider'
    }
    if (role === 'driver') {
        return 'Driver'
    }
    if (role === 'support_staff') {
        return 'Support Staff'
    }
    return null
} 

export default function LoginPage( {onLogin}: LoginPageProps) {
    const [message, setMessage] = useState("")

    return (
        <main className='login-page'>
            <img src={logo} alt="" width={350}/>
            <div className='login-card'>
            <h1>Sign-In</h1>
            <form
                method="post"
                onSubmit={async (event) => {
                    event.preventDefault()
                    const formData = new FormData(event.currentTarget)
                    const email = formData.get('email')
                    const password = formData.get('password')
                    setMessage('Signing In...')

                    try {
                        const response = await fetch('/api/login', {
                            method: 'POST',
                            headers: {'Content-Type': 'application/json'},
                            body: JSON.stringify({email, password}),
                        })

                        if (response.status === 401) {
                        setMessage("Email or password is incorrect")
                    }   else if (response.ok) {
                        const account = await response.json()

                        if (typeof account?.first_name !== 'string') {
                            setMessage("Missing first name!")
                            return
                        }
                        const role = formatRole(account.role)

                        if (role === null) {
                            setMessage("Unknown role selected!")
                            return
                        }
                        onLogin({firstName: account.first_name, role})
                    }   else {
                        setMessage(`Login request failed (${response.status}).`)
                    }
                    } catch {
                        setMessage("Error: Couldn't reach server!")
                    }
                    
                }}>
                <label htmlFor="email"> Email address </label>
                <input
                    id="email"
                    name="email"
                    type="email"
                    autoComplete="username"
                    required
                />
                <label htmlFor="password"> Password </label>
                <input
                    id="password"
                    name="password"
                    type="password"
                    autoComplete="current-password"
                    required
                />
                <button type="submit">Sign In</button>
            </form>
            <p role="status">{message}</p>
            </div>
        </main>
    )
}