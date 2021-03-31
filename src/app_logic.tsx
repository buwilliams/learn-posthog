import { kea } from 'kea'

const logic = kea({
    actions: {
        increment: (amount: any) => ({ amount }),
    },
    reducers: {
        counter: [0, { 
            increment: (state: any, { amount }: any) => state + amount,
        }]
    }
})

export default logic