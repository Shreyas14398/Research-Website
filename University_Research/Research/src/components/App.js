import React from 'react';
import ReactDOM from 'react-dom';

var Message1=[{
    "model": "Research.announcement", "pk": 1,
    "fields": {"title": "We are ON!", "body": "Finally, we are ON!"}
}];

class AppDis extends React.Component{
    render(){
        return(
            <div>
                <h1>{this.props.title}</h1>
                <h3>{this.props.body}</h3>
            </div>
        );
    }
};
class App extends React.Component{
    render(){
        var allAnn=this.props.Message.map(function(dis){
            return(
                <AppDis title={dis.fields.title} body={dis.fields.body}/>
            );
        });
        return(
          <div>
            {allAnn}
          </div>
        );
    }
};

ReactDOM.render(<App Message={Announcements}/>,document.getElementById('app1'));