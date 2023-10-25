package lab.models;

import lab.utils.Consts;

public class Patient {
    public final int id;
    public int type;
    public final double startTime;
    public double timeInLine;

    public Patient (int id, double chance, double startTime) {
        if (chance <= .5)           type = Consts.PatientTypes.toHospitalRoom;
        else if (chance <= .5 + .1) type = Consts.PatientTypes.toLab2;
        else                        type = Consts.PatientTypes.toLab3;

        this.startTime = startTime;
        this.id = id;
    }
}
