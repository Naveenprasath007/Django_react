import React, { Component } from "react";
import ReactDOM from "react-dom";
import Header from './layout/header';

class App extends Component{
    render(){
        return(
            <Header />
        )
    }
}
ReactDOM.render(<App />,document.getElementById('app'));