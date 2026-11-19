type WelcomePageProps = {
    firstName: string
    role: 'Rider' | 'Driver' | 'Support Staff'
}

export default function WelcomePage({ firstName, role }: WelcomePageProps) {
    return (
        <main>
            <h1> {role} Dashboard</h1>
            <p>Welcome, {firstName}</p>
        </main>
    )
}