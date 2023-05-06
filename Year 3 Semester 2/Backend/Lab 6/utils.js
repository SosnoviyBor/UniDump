function allBodyKeysExist(expectedKeys, body, res) {
    if (!expectedKeys.every(item => body.hasOwnProperty(item))) {
        res.status(400).send(`Wrong keys provided\n
                Expected values are [${expectedKeys}]\n
                Received keys are [${Object.keys(body)}]`)
        return false
    }
    return true
}

module.exports = {
    allBodyKeysExist
}