import React from 'react';
import ReactDOM from 'react-dom';

class Single extends React.Component{
  render(){
    return(
      <li key={this.props.key} class="anno">
      <button class="accordion"><h3><br/>{this.props.title}</h3></button>
        <div class="announcement">
        <h2>{this.props.adate}</h2>
        <h3><br/>{this.props.body}<br/><br/></h3>
        </div>
      </li>
    );
  }
};
class Pagination extends React.Component{
  constructor(props){
    super(props);
    this.state={
       currentPage:1,
       ItemsPP:5 //Items Per Page
    };
    this.PrevPage=this.PrevPage.bind(this);
    this.NextPage=this.NextPage.bind(this);
    this.handleClick=this.handleClick.bind(this);
    this.setItemsPP=this.setItemsPP.bind(this);
  }
  setItemsPP(event){
    this.setState({ItemsPP:Number(event.target.value)});
  }
  NextPage(){
    this.setState({currentPage:this.state.currentPage+1});
  }
  PrevPage(){
    this.setState({currentPage:this.state.currentPage-1});
  }
  handleClick(event){
    this.setState({currentPage:Number(event.target.id)})
  }
  render(){
    const LastIndex=this.state.currentPage*this.state.ItemsPP;
    const FirstIndex=LastIndex-this.state.ItemsPP;
    //The items to be paginated are passed as props to the Pagination instance
    const listItems=this.props.Announcements; //Allocating the data items to a constant
    const currentItems=listItems.slice(FirstIndex,LastIndex);
    const renderItems=currentItems.map((item,index)=>{
      return <Single key={index} title={item.fields.title} adate={item.fields.adate} body={item.fields.body}/>;
    });
    const pages=[];
    const total=Math.ceil(listItems.length/this.state.ItemsPP); //Finding the total number of pages
    for(let i=1;i<=total;i++){
      pages.push(i);
    }

    const renderPages=pages.map(page=>{
      return(
        <li key={page}
        id={page}
        onClick={this.handleClick} className={page==this.state.currentPage?"curpage":"page"}>
        {page}
        </li>
      );
    });
    var prev="";
    if(this.state.currentPage===1){
     prev=<a className="buttonprevdis">Previous</a>;
    }
    else{
     prev=<a className="buttonprev" onClick={this.PrevPage}>Previous</a>;
    }
    var next="";
    if(this.state.currentPage===total){
     next=<a className="buttondis">Next</a>;
    }
    else{
     next=<a className="button" onClick={this.NextPage}>Next</a>;
    }
    return (
      <div>
        <ul>
        {renderItems}
        </ul>
<br/><br/>
        <div className="paginate">
       <div>
        {prev}
       </div>
       <div>
       <ul className="pages">
       {renderPages}
       </ul>
       </div>
       <div>
       {next}
       </div>
       </div>
<br/>
<div>
        <p className="content">Items per Page:</p>
        <select className="content-select" name="Itemspp" onClick={this.setItemsPP}>
         <option value="5">5</option>
         <option value="10">10</option>
         <option value="15">15</option>
         <option value="20">20</option>
         <option value="25">50</option>
         </select>
</div>
      </div>
    );
  }
};

export default Pagination;
