import { useState } from 'react'

export default function LoginPage() {
    const [message, setMessage] = useState("")

    return (
        <main>
            <h1>Sign in to NittanyRide</h1>
            <form
                method="post"
                onSubmit={(event) => {
                    event.preventDefault()
                    const formData = new FormData(event.currentTarget)
                    const email = formData.get('email')
                    setMessage(`Form submitted for ${email}`)
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
        </main>
    )
}