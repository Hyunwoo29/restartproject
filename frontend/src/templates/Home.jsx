import React, {useState} from 'react'


const Home = ({children}) => (<>
    <table className="tab_lay">
        <tr><td><h1>홈</h1></td></tr>
        <tr><td><button >서버 연결 테스트</button></td></tr>
    </table>
    {children}

</>)


export default Home


export const Counter = () => {
    const [ number, setNumber ] = useState(0)

    return (<>
    <h1> { number }</h1>
    <button onClick = { () => setNumber( number + 1)}> + </button>
    <button onClick = { () => setNumber( number - 1)}> - </button>
</>)
}
