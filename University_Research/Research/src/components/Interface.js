import React from 'react';
import ReactDOM from 'react-dom';
import Pagination from './Pagination';
import AutoComplete from './AutoComplete';

class Interface extends React.Component{
    render(){
       var renderComp="";
       const compt=this.props.CompType;
       const compd=this.props.CompData;
       if(compt==="announcements")
       {
           renderComp=<Pagination Announcements={compd}/>;
       }
       else if(compt==="search")
       {
           renderComp=<AutoComplete List={compd}/>;
       }
       return(
           <div>
             {renderComp}
           </div>
       );
    }
}

ReactDOM.render(<Interface CompData={CompData} CompType={CompType}/>,document.getElementById('react'));