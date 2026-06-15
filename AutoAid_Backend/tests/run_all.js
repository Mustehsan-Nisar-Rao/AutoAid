// tests/run_all.js
const testReg = require('./test_registration');
const testOtpPrv = require('./test_otp_provider');
const testServices = require('./test_services');
const testRouteContactPay = require('./test_route_contact_payment');

async function main() {
    console.log('================================================================');
    console.log('              STARTING AUTOAID IDT AUTOMATED RUNNER             ');
    console.log('================================================================\n');

    await testReg.run();
    await testOtpPrv.run();
    await testServices.run();
    await testRouteContactPay.run();

    console.log('================================================================');
    console.log('             AUTOAID IDT AUTOMATED RUNNER FINISHED              ');
    console.log('================================================================\n');
}

main().catch(console.error);
