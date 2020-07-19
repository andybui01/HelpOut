import React, {Component} from 'react'
import ListView from './ListView' 
import ReactLoading from 'react-loading'


async function getListings (number, suburb){
    const axios = require('axios')
    const response = await axios.get("http://127.0.0.1:5000/listings", {params: {num:number, suburb:suburb}})
    console.log(response.data)
    return response.data    
}

class Volunteer extends Component{
    state = {
        listings:[ // Loading into this json list will load onto the listings view.
        {
            title: 'example',
            desc: 'here is an example thing ',
            Suburb: 'nup'
        },
        {
            title: "Loading..",
            desc: "Please be patient...",
            Suburb: "a"
        }
        ],
    }

    componentDidMount(){
        setTimeout(() => {
            getListings(5, "Kensington").then(response => this.setState({listings:response}))
                .then(json => this.setState({done:true}))
        }, 1200)
    }

    render() {
        //await console.log(getListings(1, "Kensington"))//this.state
        //console.log(getListings(1, "Kensington"))
        //test = getListings(1, "Kensington")//this.state
        const{listings} = this.state
        return (/*
            <div className="container">
                <h1> Help Out! </h1>
                <ListView listings={listings} adminRemoveListing={this.adminRemoveListing} / >
            </div>
            */
            <div>
            {!this.state.done? (
                <ReactLoading type={"bars"} color={"white"} />
            ):(<>
                <h1> Help Out! </h1>
                <ListView listings={listings}/> </>
            )}
            </div>
        )
    }
}
export default Volunteer
