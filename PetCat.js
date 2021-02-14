class cat {
    constructor() {
        this._tiredness = 0;
        this._hunger = 0;
        this._loneliness = 0;
        this._happiness = 0;
    }

    feed(stomach, happy) {
        this._tiredness -= stomach;
        this._happiness += happy;
    }

    sleep(tired, happy) {
        this._tiredness -= tired;
        this._happiness += happy;
    }

    pet(lonely, happy) {
        this._loneliness -= lonely;
        this._happiness += happy;
    }

    theStatus() {
        if (this._tiredness >= 0) {
            console.log("Paws is VERY tired.");
        } else {
            console.log("Paws is not tired");
        }
        if (this._hunger >= 0) {
            console.log("Paws is really hungry.");
        } else {
            console.log("Paws is not hungry.");
        }
        if (this._loneliness >= 0) {
            console.log("Paws is VERY lonely.");
        } else {
            console.log("Paws is not lonely.");
        }
        if (this._happiness <= 0) {
            console.log("Paws is not happy.")
        } else {
            console.log("Paws is VERY happy.")
        }
    }
}