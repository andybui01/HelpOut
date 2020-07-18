import React, {Component} from 'react'
import ListView from './ListView' 

async function getListings (number, suburb){
    const axios = require('axios')
    const response = await axios.get("/listings", {params: {num:number, suburb:suburb}})
    console.log(response)
    return response    
}

class Volunteer extends Component{
    //listings = getListings(10, 'Kensington')

    state = {
        listings://getListings(10,'Kensignton') [ // Loading into this json list will load onto the listings view.
        [
        {
            title: 'example',
            desc: 'here is an example thing ',
            generalLocation: 'nup'
        },
        ],
    }

    adminRemoveListing = (index) => {
        const {listings} = this.state

        this.setState({
            listings: listings.filter((listing, i)=>{
                return i !== index
            })
        })
    }
    render() {
        const {listings} = this.state

        return (
            <div className="container">
                <h1> Help Out! </h1>
                <ListView listings={listings} adminRemoveListing={this.adminRemoveListing}/>
            </div>
        )
    }
}
export default Volunteer
