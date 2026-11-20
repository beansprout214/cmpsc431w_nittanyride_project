import type { UserPageProps } from "../types";

export default function SupportStaffPage({firstName}: UserPageProps) {
    return (
        <main>
            <h1>Support Staff Dashboard</h1>
            <p>Welcome, {firstName}</p>
        </main>
    )
}