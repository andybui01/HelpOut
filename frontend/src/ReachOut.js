import React, {Component} from 'react'

async function createListing(){
    const axios = require('axios')
    const form = new FormData()
    form.set('')

}
/*
		request.form.get('personID'),
		request.form.get('title'),
		request.form.get('desc'),
		request.form.get('commitment'),
		request.form.get('location')
*/
const Form = (props) => {
    return(
    <>
    <form>
        <label htmlFor="title">Title your request.</label>
        <input type="text" name="title" id="title" value = {title}>
        <label htmlFor="desc">Describe your request.</label>
        <input type="text" name="desc" id="desc" value = {desc}>
        <label htmlFor="commitment">How long will you need?</label>
        <input type="text" name="commitment" id="commitment" value = {commitment}>
        <label htmlFor="suburb">What suburb are you based?</label>
        <input type="text" name="suburb" id="suburb" value = {suburb}>
    </form>
    </>
    )
}

export default ReachOut
