import { useState } from 'react'
import axios from 'axios';

function App() {
  const [username, setUsername] = useState("")
  const [password, setPassword] = useState("")

  const handleSubmit = async (e) => {
    e.preventDefault()
    const data = { username, password }
    try {
      const res = await axios.post('/login/api/login', data);
      console.log(res.data)
    } catch (error) {
      console.log(error)
    }
    
  }

  return (
    <>
      <div className="grid place-items-center min-h-screen min-w-screen">
        <form className="border flex flex-col w-[30rem] h-[20rem]" onSubmit={handleSubmit}>
          <div className="flex-1 flex flex-col justify-center px-10 py-10 gap-10 w-full text-center">
            <h1 className="text-xl font-bold">JWT Login</h1>
            <input 
              type="text" 
              placeholder="Username" 
              className="border p-4"
              value={username}
              onChange={(e) => setUsername(e.target.value)}/>
            <input 
              type="password" 
              placeholder="Password" 
              className="border p-4" 
              value={password}
              onChange={(e) => setPassword(e.target.value)}/>
          </div>
          <button className="bg-green-500 hover:bg-green-600 p-4 w-full">Sign In</button>
        </form>
      </div>
    </>
  )
}

export default App
