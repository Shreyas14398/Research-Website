import React from 'react';
import ReactDOM from 'react-dom';
import './SupComplete.css';

class SupComplete extends React.Component{
	constructor(props){
		super(props);
		this.state={
			selected:"0",
			typed:"",
			shortList:[]
		};
		this.keyReturn=this.keyReturn.bind(this);
    this.keyDown=this.keyDown.bind(this);
    this.keyInput=this.keyInput.bind(this);
		this.handleClick=this.handleClick.bind(this);
	}
	handleClick(event){
        this.setState({typed:event.target.id,shortList:[]})
	}
  keyInput(){
           const size=document.getElementById("search").value.length;
           const total=this.props.List.length;
           var smallList=[];
           var subword=document.getElementById("search").value;
           if(size===0){
             this.setState({typed:subword,shortList:smallList});
           }
           else{
           for(let i=0;i<total;i++)
           {
             const cmpstrno=this.props.List[i].fields.supervisor.substring(0,size);
             const cmpstrletter=this.props.List[i].fields.name.substring(0,size);
             if(subword===cmpstrno)
             {
              smallList.push(this.props.List[i]);
             }
             else if(subword.toUpperCase()===cmpstrletter.toUpperCase())
             {
               smallList.push(this.props.List[i]);
             }
             this.setState({typed:subword,shortList:smallList});
           }
         }
        }
	keyReturn(event){
        var check=(event.keyCode?event.keyCode:event.which);
        if(check===13) //Enter key
        {  
           if(this.state.selected!=="0")
          {	
           this.setState({typed:this.state.selected.fields.supervisor,shortList:[]}); 
          }  //If user wishes to select the current value from dropdown
        }
        }
  keyDown(event){
         var check=(event.keyCode?event.keyCode:event.which);
         if(check===38) //Up key
        {
          if(this.state.shortList.length!==0)
               {
                  const len=this.state.shortList.length;
                  var j=len;
                  for(let i=len-1;i>=0;i--)
                 {
                     if(this.state.selected===this.state.shortList[i])
                     {
                        j=i; 
                     }
                 }
                 j=j-1;
                 if(j>=0)
                 {
                   this.setState({selected:this.state.shortList[j]});
                 }
                 else if(j<0)
                 {
                  this.setState({selected:"0"});
                 }
               }
        }
         else if(check===40)  //Down key
        {
          if(this.state.shortList.length!==0)
		{   
			const len=this.state.shortList.length;
			var j=-1;
			for(let i=0;i<len;i++)
			{
				if(this.state.selected===this.state.shortList[i])
				{
					j=i;
				}
			}
                        j=j+1;
                        if(j<len)
                       {
			this.setState({selected:this.state.shortList[j]});
                       }
		}
        }
        }
	render()
	{
        var dis="block";
        if(this.state.shortList.length===0)
        {
          dis="none";
        } 
        if(this.state.typed.length!==0)
        {
          document.getElementById('search').value=this.state.typed;
        }
        const renderList=this.state.shortList.map((short,index)=>{
        	return(
        		<li key={index} className={(short===this.state.selected)?"selected":"unselected"} id={short.fields.supervisor} onClick={this.handleClick}>{short.fields.supervisor}-{short.fields.name}</li>
        		);
        });
		return (
			<div className="typeBox">
			 <input id="search" type="text" onInput={this.keyInput} onKeyPress={this.keyReturn} onKeyDown={this.keyDown} tabIndex="0" className="searchBox"/>
			 <div className="suggestions" style={{display:dis}}>
			 <ul className="ListU">
			 {renderList}
			 </ul>
			 </div>
			</div>
			);

	}
};

ReactDOM.render(<SupComplete List={dbSList}/>,document.getElementById('sureact'));
