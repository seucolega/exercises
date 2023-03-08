class Lasagna
{
    public int ExpectedMinutesInOven() => 40;

    public int RemainingMinutesInOven(int ActualTime) =>
        ExpectedMinutesInOven() - ActualTime;

    public int PreparationTimeInMinutes(int NumberOfLayers) => 
        NumberOfLayers * 2;

    public int ElapsedTimeInMinutes(int NumberOfLayers, int ActualTime) =>
        PreparationTimeInMinutes(NumberOfLayers) + ActualTime;
}
