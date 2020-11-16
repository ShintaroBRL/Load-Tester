from assets.StartUp import StartUp
from assets.request import Request
from assets.load import Load
import signal

class main:
    def __init__(init):
        startup  = StartUp()
        request = Request()
        signal.signal(signal.SIGINT, startup.keyboardInterruptHandler)
        args = startup.getArgs()
        Load(args.users ,args.sleep ,request.onStart ,request.Run ,request.OnFinish ,args.url ,args.ssl)

if __name__ == "__main__":
    main()