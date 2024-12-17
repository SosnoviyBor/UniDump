from utils.consts import OPERATION_SPEED


class DiagramBuilder:

    def __init__(self, processes:int):
        self.processes = processes
        self.step = 0


    def header(self) -> str:
        columnNumbers = ""
        for i in range(1, self.processes + 1):
            columnNumbers += f"  {i} "
            
        msg = (" " + columnNumbers +"\n" +
               "┌" + ("────" * self.processes) + "─┐ New action!")
        
        return msg


    def body(self, symbol:str, times:int) -> str:
        msg = ""
        
        if self.step != 0:
            msg += "├" + ("────" * self.processes) + "─┤ New action!\n"
        
        for _ in range(OPERATION_SPEED[symbol]):
            self.step += 1
            
            msg += (
                # step + border
                "│ "+
                # active cell
                f"[{symbol}] " * times +
                # inactive cell
                "[ ] " * (self.processes - times) +
                # border + step
                f"│ {self.step}\n")
        
        return msg[:-1]
    
    
    def bottom(self) -> str:
        return "└" + ("────" * self.processes) + "─┘"