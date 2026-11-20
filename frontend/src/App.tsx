import { useState } from 'react'
import LoginPage from './pages/LoginPage'
import RiderPage from './pages/RiderPage'
import type { UserPageProps } from './types'
import DriverPage from './pages/DriverPage'
import SupportStaffPage from './pages/SupportStaffPage'

export default function App() {
  const [user, setUser] = useState<UserPageProps | null>({
    firstName: 'Ryan',
    role: 'Support Staff'
  }
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
  // formatRole() Does checks for role validity so this structure is okay. 
  return <SupportStaffPage {...user}/>
}