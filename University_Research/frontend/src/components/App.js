import React from 'react';
import ReactDOM from 'react-dom';

class App extends React.Component{
    render(){
        return(
        <p>Hello+{this.props.Message}</p>
        );
    }
};

ReactDOM.render(<App Message={Message}/>,document.getElementById('app'));