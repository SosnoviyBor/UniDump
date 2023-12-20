package LibTest;

import java.util.ArrayList;
import PetriObj.*;

public class Task3 {

    public static void main(String[] args) throws
            ExceptionInvalidTimeDelay, ExceptionInvalidNetStructure {
        PetriObjModel model = getModel();
        model.setIsProtokol(false);
        double timeModeling = 1000;
        model.go(timeModeling);
        System.out.println("Declines: " + model.getListObj().get(0).getNet().getListP()[2].getMark());
        System.out.println("Trips: " + countTotalTrips(model));
        /* for (int i = 0; i < model.getListObj().size(); i++) {
            model.getListObj().get(i).printMark();
        }*/
    }

    private static int countTotalTrips(PetriObjModel model) {
        int count = 0;
        for (int i = 2; i < model.getListObj().size(); i++) {
            count += model.getListObj().get(i).getNet().getListP()[5].getMark();
        }
        return count;
    }

    public static PetriObjModel getModel() throws
            ExceptionInvalidNetStructure, ExceptionInvalidTimeDelay {
        ArrayList<PetriSim> list = new ArrayList<>();
        
        list.add(new PetriSim(netGenerator())); // автобусА
        list.add(new PetriSim(netGenerator())); // автобусВ
        list.add(new PetriSim(busModel(1, 20.0))); // зупинка1
        list.add(new PetriSim(busModel(1, 30.0))); // зупинка1
        list.add(new PetriSim(busModel(0, 20.0))); // зупинка2
        list.add(new PetriSim(busModel(0, 30.0))); // зупинка2
        
        list.get(2).setPriority(1);
        list.get(4).setPriority(1);
        
        list.get(2).getNet().getListP()[0] = list.get(0).getNet().getListP()[3]; // зупинка1 -> автобусА
        list.get(3).getNet().getListP()[0] = list.get(0).getNet().getListP()[3]; // зупинка1 -> автобусВ
        list.get(4).getNet().getListP()[0] = list.get(1).getNet().getListP()[3]; // зупинка2 -> автобусА
        list.get(5).getNet().getListP()[0] = list.get(1).getNet().getListP()[3]; // зупинка2 -> автобусВ
        list.get(1).getNet().getListP()[2] = list.get(0).getNet().getListP()[2];
        list.get(4).getNet().getListP()[1] = list.get(2).getNet().getListP()[4];
        list.get(4).getNet().getListP()[4] = list.get(2).getNet().getListP()[1];
        list.get(5).getNet().getListP()[1] = list.get(3).getNet().getListP()[4];
        list.get(5).getNet().getListP()[4] = list.get(3).getNet().getListP()[1];
        return new PetriObjModel(list);
    }

    public static PetriNet netGenerator() throws
            ExceptionInvalidNetStructure, ExceptionInvalidTimeDelay {
        ArrayList<PetriP> places = new ArrayList<>();
        ArrayList<PetriT> transitions = new ArrayList<>();
        ArrayList<ArcIn> arcIns = new ArrayList<>();
        ArrayList<ArcOut> arcOuts = new ArrayList<>();
        
        places.add(new PetriP("P1", 1));
        places.add(new PetriP("P2", 0));
        places.add(new PetriP("decline", 0));
        places.add(new PetriP("queue", 0));
        
        transitions.add(new PetriT("T1", 0.5));
        transitions.get(0).setDistribution("norm", transitions.get(0).getTimeServ());
        transitions.get(0).setParamDeviation(0.2);
        transitions.add(new PetriT("changeBus", 0.0));
        transitions.get(1).setPriority(1);
        transitions.add(new PetriT("toQueue", 0.0));
        
        arcIns.add(new ArcIn(places.get(0), transitions.get(0), 1));
        arcIns.add(new ArcIn(places.get(1), transitions.get(1), 1));
        arcIns.add(new ArcIn(places.get(1), transitions.get(2), 1));
        arcIns.add(new ArcIn(places.get(3), transitions.get(1), 30));
        arcIns.get(3).setInf(true);
        arcOuts.add(new ArcOut(transitions.get(0), places.get(0), 1));
        arcOuts.add(new ArcOut(transitions.get(0), places.get(1), 1));
        arcOuts.add(new ArcOut(transitions.get(1), places.get(2), 1));
        arcOuts.add(new ArcOut(transitions.get(2), places.get(3), 1));
        
        PetriNet petriNet = new PetriNet("creationModel", places, transitions, arcIns, arcOuts);
        PetriP.initNext();
        PetriT.initNext();
        ArcIn.initNext();
        ArcOut.initNext();
        return petriNet;
    }

    public static PetriNet busModel(int n, double t) throws
            ExceptionInvalidNetStructure, ExceptionInvalidTimeDelay {
        ArrayList<PetriP> places = new ArrayList<>();
        ArrayList<PetriT> transitions = new ArrayList<>();
        ArrayList<ArcIn> arcIns = new ArrayList<>();
        ArrayList<ArcOut> arcOuts = new ArrayList<>();
        
        places.add(new PetriP("queue", 0));
        places.add(new PetriP("city1AvailableBus", n));
        places.add(new PetriP("places", 0));
        places.add(new PetriP("finishedDeliver", 0));
        places.add(new PetriP("city2AvailableBus", 0));
        places.add(new PetriP("completed", 0));
        
        transitions.add(new PetriT("doSit", 0.0));
        transitions.get(0).setPriority(1);
        transitions.add(new PetriT("doDrive", t));
        transitions.get(1).setDistribution("norm", transitions.get(1).getTimeServ());
        transitions.get(1).setParamDeviation(5.0);
        transitions.add(new PetriT("exit", 0.0));
        
        arcIns.add(new ArcIn(places.get(0), transitions.get(0), 1));
        arcIns.add(new ArcIn(places.get(1), transitions.get(0), 1));
        arcIns.get(1).setInf(true);
        arcIns.add(new ArcIn(places.get(2), transitions.get(1), 20));
        arcIns.add(new ArcIn(places.get(3), transitions.get(2), 1));
        arcIns.add(new ArcIn(places.get(1), transitions.get(1), 1));
        arcOuts.add(new ArcOut(transitions.get(0), places.get(2), 1));
        arcOuts.add(new ArcOut(transitions.get(1), places.get(3), 1));
        arcOuts.add(new ArcOut(transitions.get(2), places.get(4), 1));
        arcOuts.add(new ArcOut(transitions.get(2), places.get(5), 20));
        
        PetriNet petriNet = new PetriNet("busModel", places, transitions, arcIns, arcOuts);
        PetriP.initNext();
        PetriT.initNext();
        ArcIn.initNext();
        ArcOut.initNext();
        return petriNet;
    }
}
