const winston = require('winston');


const logger = winston.createLogger({
    level: 'info',
    format: winston.format.json(),
    defaultMeta: { service: 'user-service' },
    transports: [
      //
      // - Write all logs with importance level of `error` or less to `error.log`
      // - Write all logs with importance level of `info` or less to `combined.log`
      //
      new winston.transports.File({ filename: 'error.log', level: 'error' }),
      new winston.transports.File({ filename: 'combined.log' }),
    ],
  });

logger.error('error');
logger.warn('warn');
logger.info('info');
console.log('log');
logger.debug('debug');


const dobleNumero = val =>{
    if (typeof val === 'number'){
        return 2 * val;
    
    }
    throw new Error("El valor debe ser tipo numero")
}


const numero = 8;

try{
    console.log("Ejecutandose correctamente");
    const doble = dobleNumero(numero);
    console.log(doble);
}   
catch(e){
    console.log("error");
    logger.error(e.message);
}


