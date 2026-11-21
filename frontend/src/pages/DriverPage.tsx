import type { UserPageProps } from "../types";

export default function DriverPage({firstName}: UserPageProps) {
    return (
        <main>
            <h1>Driver Dashboard</h1>
            <p>Welcome, {firstName}</p>
        </main>
    )
}