import { useState } from 'react'
import LoginPage from './pages/LoginPage'
import RiderPage from './pages/RiderPage'
import type { UserPageProps } from './types'
import DriverPage from './pages/DriverPage'
import SupportStaffPage from './pages/SupportStaffPage'

export default function App() {
  const [user, setUser] = useState<UserPageProps | null>(null
  )

  if (user === null) {
    return <LoginPage onLogin= {setUser}/>
  }
  if (user.role === 'Rider') {
    return <RiderPage {...user}/>
  }
  if (user.role === 'Driver') {
    return <DriverPage {...user}/>
  }
  // formatRole() in LoginPage.tsx checks for role validity so this structure isn't as dumb as it looks. 
  return <SupportStaffPage {...user}/>
}