import { useState } from 'react'
import type { UserPageProps } from '../types'


type Ride = {
    id:number
    description: string
    fareRate: number
}
const sampleRides: Ride[] = [
    { id: 1, description: 'Airport shuttle from campus', fareRate: 12 },
    { id: 2, description: 'Evening ride to downtown State College', fareRate: 8 },
]

export default function WelcomePage({ firstName, role }: UserPageProps) {
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
                        const keyword = String(formData.get('keyword') ?? "").trim()

                        if (keyword === '') {
                            setResults([])
                            setSearchMethod("Enter Destination")
                            return
                        }
                        const matches = sampleRides.filter((ride) => {
                            return ride.description.toLowerCase().includes(keyword.toLowerCase())
                        })

                        setResults(matches)

                        if (matches.length === 0 ) {
                            setSearchMethod(`No rides found for ${keyword}`)
                        } else{
                            setSearchMethod(`Rides found: ${matches.length } `)                       }
                    }}>
                        <label htmlFor = "keyword">Where are you going?</label>
                        <input id="keyword" name="keyword" type="text"/>
                        <button type = "submit">Search rides</button>
                    </form>
                    <p role="status">{searchMethod}</p>
                    {results.length > 0 && (
                        <ul>
                            {results.map((ride) => (
                                <li key={ride.id}>
                                    {ride.description} - ${ride.fareRate.toFixed(2)}
                                </li>
                            ))}
                        </ul>
                    )}
                </section>
            )}
        </main>
    )
}