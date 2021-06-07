import React from 'react'
import { Route } from "react-router-dom"
import { counter } from 'counter/index'
import { Login, SignUp, UserDetail, UserEdit, UserList} from 'user/index'
import { Home } from 'common/index'


const App = () => {
  return (<div>
    <Route exact path='/common' component={Home}/>
    <Route exact path='/counter' component={counter}/>
    <Route exact path='/user-list' component={UserList}/>
    <Route exact path='/login' component={Login}/>
    <Route exact path='/signup' component={SignUp}/>
    <Route exact path='/user-detail' component={UserDetail}/>
    <Route exact path='/user-edit' component={UserEdit}/>
  </div>)
}

export default App