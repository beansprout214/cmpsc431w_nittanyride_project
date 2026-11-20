import { useState } from 'react'


export type WelcomePageProps = {
    firstName: string
    role: 'Rider' | 'Driver' | 'Support Staff'
}

type Ride = {
    id:number
    origin: string
    destination: string
}
const sampleRides: Ride[] = [
    { id: 1, origin: 'Altoona', destination: 'State College' },
    { id: 2, origin: 'State College', destination: 'Pittsburgh' },
]

export default function WelcomePage({ firstName, role }: WelcomePageProps) {
    const [searchMethod, setSearchMethod] = useState('')
    const [results, setResults] = useState<Ride[]>([])


    return (
        <main>
            <h1> {role} Dashboard</h1>
            <p>Welcome, {firstName}</p>
            {role == 'Rider' && (
                <section>
                    <h2> Find a ride</h2>
                    <form onSubmit={(event) => {
                        event.preventDefault()
                        const formData = new FormData(event.currentTarget)
                        const destination = String(formData.get('destination') ?? "").trim()

                        if (destination === '') {
                            setResults([])
                            setSearchMethod("Enter Destination")
                            return
                        }
                        const matches = sampleRides.filter((ride) => {
                            return ride.destination.toLowerCase() === destination.toLowerCase()
                        })

                        setResults(matches)

                        if (matches.length === 0 ) {
                            setSearchMethod(`No rides found to ${destination}`)
                        } else{
                            setSearchMethod(`Rides found: ${matches.length } `)                       }
                    }}>
                        <label htmlFor = "destination">Where are you going?</label>
                        <input id="destination" name="destination" type="text"/>
                        <button type = "submit">Search rides</button>
                    </form>
                    <p role="status">{searchMethod}</p>
                    {results.length > 0 && (
                        <ul>
                            {results.map((ride) => (
                                <li key={ride.id}>
                                    {ride.origin} {'->'} {ride.destination}
                                </li>
                            ))}
                        </ul>
                    )}
                </section>
            )}
        </main>
    )
}