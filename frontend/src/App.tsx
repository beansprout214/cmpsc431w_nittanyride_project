import { useState } from 'react'
import LoginPage from './pages/LoginPage'
import WelcomePage, {type WelcomePageProps} from './pages/WelcomePage'

export default function App() {
  const [user, setUser] = useState<WelcomePageProps | null>(
  null)

  if (user === null) {
    return <LoginPage onLogin= {setUser}/>
  }

  return <WelcomePage firstName={user.firstName} role={user.role}/>
}