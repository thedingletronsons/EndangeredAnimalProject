import React from 'react';
import { BrowserRouter as Router, Switch, Route} from 'react-router-dom';
import './App.css';
import Navbar from './components/Navbar';
import Home from './components/pages/Home';
import Model from './components/pages/Model';
import SignUp from './components/pages/Sign-up';
import DataBase from './components/pages/DataBase';

function App() {
    return(
        <>
        <Router>
            <Navbar/>
            <Switch>
                <Route path='/' exact component={Home}/>
                <Route path='/model' component={Model}/>
                <Route path='/sign-up' component={SignUp}/>
                <Route path='/DataBase' component={DataBase}/>
            </Switch>
        </Router>
        </>
    );
}

export default App;